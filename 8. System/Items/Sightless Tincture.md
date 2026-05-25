---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 115}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

With an incredibly deep black hue, sightless tincture is usually [[Concealed]] in wine, blood pudding, or other darkly colored foods. The oil at first faintly dims its victim's sight, then blacks it out entirely.

**Saving Throw** DC 28 [[Fortitude]] save

**Onset** 10 minutes

**Maximum Duration** 14 hours

**Stage 1** [[Dazzled]] and a –2 status penalty to visual Perception checks (1 hour)

**Stage 2** dazzled and a –4 status penalty to visual Perception checks (1 hour)

**Stage 3** [[Blinded]] (2d6 hours); stage 3 is an incapacitation effect, and if the victim is still blinded from the poison when the poison has run its course, the blindness lasts for an additional 24 hours afterward

**Source:** `= this.source` (`= this.source-type`)
