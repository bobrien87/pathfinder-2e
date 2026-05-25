---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 38000}"
usage: "worn"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The superior adamantine-lead alloy known as keep stone is as highly prized as it is expensive, and for good reason: keep stone combines the Hardness and durability of the finest metal with inherent magical protection. Not only does the metal itself resist magical effects, but anyone in proximity to a large amount of it also enjoys a degree of protection from divination magic. Dwarven crafters have attempted to make this extra protection more portable and more affordable in the form of *keep stone amulets*. Each amulet is unique in its exact shape, size, thickness, and decorations, but typically, a keep stone amulet is roughly palm-sized and engraved with clan symbols, holy aphorisms, or a favorite line of poetry.

While wearing a *keep stone amulet*, if you're the target of a spell with the detection or scrying trait, the caster must succeed at a DC 5 flat check or lose the spell.

**Activate—Rebuff Magic** `pf2:r` (concentrate, misfortune)

**Frequency** once per day

**Trigger** You're the target of a spell with a spell attack roll

**Effect** The caster must roll the spell attack roll twice and take the worse result.

**Source:** `= this.source` (`= this.source-type`)
