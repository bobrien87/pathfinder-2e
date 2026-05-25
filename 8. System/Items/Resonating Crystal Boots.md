---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 475}"
usage: "worn"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These supple leather boots are studded with tiny crystals.

**Activate—Chiming Steps** `pf2:1` (auditory, concentrate, sonic)

**Frequency** once per day

**Effect** Stride up to half your Speed. The crystals ring out with pleasant-sounding chimes that reverberate painfully in the ears of others. Each creature that you pass adjacent to during your Stride takes 4d8 sonic damage (DC 24 [[Fortitude]] save); a creature takes this damage only once. A creature who critically fails the save is also [[Deafened]] for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
