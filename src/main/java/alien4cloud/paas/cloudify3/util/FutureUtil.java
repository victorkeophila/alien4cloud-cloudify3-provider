package alien4cloud.paas.cloudify3.util;

import org.springframework.http.ResponseEntity;

import alien4cloud.paas.IPaaSCallback;

import com.google.common.base.Function;
import com.google.common.util.concurrent.FutureCallback;
import com.google.common.util.concurrent.Futures;
import com.google.common.util.concurrent.ListenableFuture;

public class FutureUtil {

    public static <T> ListenableFuture<T> unwrapRestResponse(org.springframework.util.concurrent.ListenableFuture<ResponseEntity<T>> future) {
        ListenableFuture<ResponseEntity<T>> guavaFuture = toGuavaFuture(future);
        return Futures.transform(guavaFuture, new Function<ResponseEntity<T>, T>() {
            @Override
            public T apply(ResponseEntity<T> input) {
                return input.getBody();
            }
        });
    }

    public static <T> ListenableFuture<T> toGuavaFuture(org.springframework.util.concurrent.ListenableFuture<T> future) {
        return new SpringToGuavaListenableFuture<>(future);
    }

    public static <T> void associateFutureToPaaSCallback(ListenableFuture<T> future, final IPaaSCallback<T> callback) {
        Futures.addCallback(future, new FutureCallback<T>() {
            @Override
            public void onSuccess(T result) {
                if (callback != null) {
                    callback.onSuccess(result);
                }
            }

            @Override
            public void onFailure(Throwable t) {
                if (callback != null) {
                    callback.onFailure(t);
                }
            }
        });
    }
}
