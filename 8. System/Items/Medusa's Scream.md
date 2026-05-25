---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 3000}"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The ghastly visage of a slain medusa's head stares out from this steel shield (Hardness 13, HP 52, BT 26). The shield comes with a thick leather cover to conceal the head.

**Activate—Petrifying Gaze** `pf2:2` (manipulate, visual)

**Frequency** once per day

**Effect** You reveal the medusa's face, focusing its gaze on one creature within 30 feet. The shield casts a DC 30 [[Petrify]] spell with a range of 30 feet.

**Craft Requirements** The initial raw materials must include the head of a medusa.

HardnessHPBT135226

**Source:** `= this.source` (`= this.source-type`)
