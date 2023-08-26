import reactor.core.publisher.Mono;
import reactor.core.publisher.Sinks;

public class ChatRoom {
    private final Sinks.Many<String> messages = Sinks.many().multicast().onBackpressureBuffer();

    public void sendMessage(String message) {
        messages.emitNext(message, Sinks.EmitFailureHandler.FAIL_FAST);
    }

    public Mono<Message> receiveMessage() {
        return messages.asFlux().next();
    }
}