---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Artifact]]", "[[Invested]]", "[[Occult]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The sharpness of this dark metal splinter never dulls. By plunging it into your neck, you anchor your soul to the fragment, granting you protection from those that would harm it at the cost of weakening your body. You take a –1 status penalty to saving throws against effects that would give you the [[Clumsy]], [[Drained]], or [[Enfeebled]] condition. At 10th level, the penalty increases to –2. However, you gain spirit resistance equal to your level and a +2 status bonus to saving throws against spirits or haunts and effects that would give you the [[Confused]], [[Controlled]], [[Doomed]], or [[Stupefied]] conditions.

**Destruction** All 13 splinters of finality must be gathered and used to reconstruct *Silent Lenore*, which must then be destroyed by means of the [[Blunt the Final Blade]] ritual.

Splinter of Finality

**Source:** `= this.source` (`= this.source-type`)
