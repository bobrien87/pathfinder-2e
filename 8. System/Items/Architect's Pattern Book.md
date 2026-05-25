---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 240}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Typically created by wizards who are hobbyists or professional architects, an architect's pattern book allows the caster to customize certain spells that create magical structures or domiciles, adding recreational areas such as an indoor bathhouse, gaming room, swimming pool, or similar luxury.

**Activate** `pf2:f` (concentrate, spellshape)

**Frequency** once per week

**Effect** If your next action is to cast a [[Cozy Cabin]], [[Planar Palace]], or [[Resplendent Mansion]] spell, you add a room to the structure that is up to 10 feet per side per rank of the spell. This room is outfitted with all the accoutrements for a particular type of recreation, determined by you when you cast the spell. Any character who spends at least 1 hour using this recreational facility and then sleeps a full 8 hours inside the location created by the spell is exceptionally well-rested. They regain double the amount of Hit Points they would normally receive for an 8-hour rest, and when they make the next day's preparations, they gain a +1 circumstance bonus to Athletics checks and Will saves for the next 12 hours.

> [!danger] Effect: Architect's Pattern Book

**Source:** `= this.source` (`= this.source-type`)
