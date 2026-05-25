---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 20000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This glittering charm is made of a gemstone flawed with a leaden inclusion. Spellcasters can cast spells into *countering charms* that they've invested or that are invested by a willing creature. The spell's effect doesn't occur; the spell's power is instead stored within the charm, replacing any spell previously there. The charm can hold only spells cast from spell slots, not cantrips or focus spells. While the charm is invested, the creature who has invested it knows what spell is stored within and automatically identifies that spell when it's cast.

**Activate—Counter** R (manipulate)

**Trigger** You are targeted by or within the area of the spell stored within the charm

**Requirements** You have a free hand

**Effect** You present the charm and attempt to counteract the triggering spell, using the rank of the spell stored in the charm and a counteract modifier of +30. This expends the spell held in the charm.

**Source:** `= this.source` (`= this.source-type`)
