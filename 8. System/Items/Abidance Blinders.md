---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 25}"
usage: "wornheadwear"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While many skilled cavalry units have their own beloved mounts, troops often need to make do with whatever animals are available for mounted combat. These blinders, made of dark brown leather, nearly cover an animal's eyes and prevent it from seeing the dangers around them.

It takes 1 minute to affix the blinders on an animal, whose attitude toward you must be indifferent or better. These blinders can be used only on a domesticated animal that doesn't have combat training or the minion trait. Animals with these blinders on do not suffer from the [[Frightened]] condition due to being in combat, nor do they automatically flee combat, as would be normal for an animal without combat training. Unless mounted by a rider with the paired headband, which is braided from the same dark brown leather, the animal's speed is reduced to 10 feet.

**Activate—It Can't Hurt You** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** An animal within 30 feet wearing the paired blinders attempts a saving throw against a fear effect but hasn't rolled yet

**Effect** You grant a +1 status bonus to its saving throw against the triggering effect.

> [!danger] Effect: It Can't Hurt You

**Source:** `= this.source` (`= this.source-type`)
