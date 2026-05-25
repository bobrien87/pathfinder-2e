---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Disarm]]", "[[Magical]]", "[[Poison]]", "[[Sweep]]", "[[Trip]]"]
price: "{'gp': 350}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

With careful alchemical treatments, orc weaponsmiths can enhance the durability and flexibility of giant scorpion tails to create multi-headed *+1 striking flails*. Additional enchantments allow the stingers to generate their own venom. When you would apply this flail's critical specialization, you can instead deal 1d6 persistent,poison damage to the target. You gain an item bonus to the persistent poison damage equal to the weapon's item bonus to attack rolls.

**Activate—Envenom** `pf2:1` (manipulate, poison)

**Frequency** once per day

**Effect** You temporarily fill the flail's stingers with venom. The next successful Strike you make with it before the end of your next turn deals 2d6 persistent,poison damage to the target. If the Strike critically succeeds and if you would apply persistent poison damage with this weapon's alternate critical specialization, you combine the two effects to deal 3d6 persistent,poison damage to the target.

**Source:** `= this.source` (`= this.source-type`)
