FROM golang:1.25 AS builder

WORKDIR /app

COPY . /app/

# 编译可执行文件
RUN CGO_ENABLED=0 GOOS=linux go build -o server ./main.go
FROM debian:bookworm-slim

# 从构建阶段复制编译好的二进制文件
COPY --from=builder /app/server .

EXPOSE 8080

CMD ["./server"]