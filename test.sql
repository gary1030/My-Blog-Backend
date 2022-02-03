select * from post;

CREATE SEQUENCE post_id_seq;
alter table post
 alter column id set default nextval('post_id_seq');
ALTER TABLE post ALTER COLUMN id SET NOT NULL;
ALTER SEQUENCE post_id_seq OWNED BY post.id;

delete from post where id=4;