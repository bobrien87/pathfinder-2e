---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Wood]]"]
price: "{'gp': 2000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ornate fan's carving depicts a particular tableau from the Plane of Wood, often of the site where the fan was created. Fanning it through the air creates a sandalwood-scented breeze and a crackling of magic. A *sandalwood fan* is a planar key for [[Interplanar Teleport]] and similar magic. The *sandalwood fan* makes it more likely for you to arrive where you intended, appearing 1d6×25 miles from your intended destination instead of the usual error range. This distance is further reduced to 1d4×25 miles if your destination is the scenery depicted on the fan.

**Activate - Plant Speech** 1 minute (manipulate)

**Frequency** once per day

**Effect** The *sandalwood fan* casts [[Speak with Plants]] and [[Translate]] for Fey and Muan on you. In addition to conversing with nearby plants, you can also communicate with any living plants you've spoken with in the past using this fan. These plants must either be on the same plane as you or on the Plane of Wood.

**Activate - Cloud of Leaves** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You summon leaves that protect your allies and identify enemies. All allies and indifferent creatures within 30 feet of you gain lesser cover for 1 round, while enemies come under the effect of [[Revealing Light]] for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
