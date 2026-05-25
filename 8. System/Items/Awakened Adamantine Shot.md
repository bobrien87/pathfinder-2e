---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 3500}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** round

**Activate** `pf2:1` (manipulate)

These bullets are formed from a liquefied high-grade precious metal and enchanted to unlock that metal's true potential.

The shot is a high-grade adamantine bullet. The awakened adamantine breaks through any resistance. The shot ignores the first 20 resistance a creature has to physical damage, all damage, or piercing or bludgeoning damage. Against a construct or creature who already has a resistance bypassed by adamantine, or a weakness to adamantine, the shot shatters the target's defenses, causing them to become [[Off Guard]] for 1 minute instead. Because adamantine is uncommon, this version of awakened metal shot is uncommon even for gunslingers or other characters with access to uncommon guns and bullets from this book.

**Source:** `= this.source` (`= this.source-type`)
