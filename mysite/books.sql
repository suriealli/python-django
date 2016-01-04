CREATE TABLE `books_publisher` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(30) NOT NULL,
    `address` varchar(50) NOT NULL,
    `city` varchar(60) NOT NULL,
    `state_province` varchar(30) NOT NULL,
    `country` varchar(50) NOT NULL,
    `website` varchar(200) NOT NULL
)
;
CREATE TABLE `books_author` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `first_name` varchar(30) NOT NULL,
    `last_name` varchar(40) NOT NULL,
    `email` varchar(254) NOT NULL
)
;
CREATE TABLE `books_book_authors` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `book_id` integer NOT NULL,
    `author_id` integer NOT NULL,
    UNIQUE (`book_id`, `author_id`)
)
;
ALTER TABLE `books_book_authors` ADD CONSTRAINT `author_id_refs_id_1a0a2829` FOREIGN KEY (`author_id`) REFERENCES `books_author` (`id`);
CREATE TABLE `books_book` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(100) NOT NULL,
    `publisher_id` integer NOT NULL,
    `publication_date` date NOT NULL
)
;
ALTER TABLE `books_book` ADD CONSTRAINT `publisher_id_refs_id_974c2a46` FOREIGN KEY (`publisher_id`) REFERENCES `books_publisher` (`id`);
ALTER TABLE `books_book_authors` ADD CONSTRAINT `book_id_refs_id_0a3634f3` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`);
CREATE INDEX `books_book_authors_36c249d7` ON `books_book_authors` (`book_id`);
CREATE INDEX `books_book_authors_e969df21` ON `books_book_authors` (`author_id`);
CREATE INDEX `books_book_81b79144` ON `books_book` (`publisher_id`);
