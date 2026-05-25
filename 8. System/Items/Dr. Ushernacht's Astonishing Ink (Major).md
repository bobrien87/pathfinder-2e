---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 2250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This syrupy ink smells organic and faintly spoiled. It's tied to one of Ushernacht's engines, created with a sample of the fluid from inside the engine. If the associated engine stops functioning, all ink linked with it can no longer be activated, including freshly created ink.

When you write a question on a sheet of paper using the astonishing ink, handwriting scrawls over the paper after 10 minutes, answering with the knowledge it can draw from its engine. The astonishing ink has all Lore skills and attempts a Recall Knowledge check to answer the question with a +28 modifier. At the GM's discretion, the astonishing ink takes a –4 circumstance penalty to the check if the question relates to advice, emotions, opinions, or other subjective topics.

If the astonishing ink fails (but not critically fails) the check to Recall Knowledge, the writing turns blood-red as it forms disturbing words. Anyone reading these words must succeed at a DC 36 [[Will]] save or become [[Stupefied 1]] until they get a full night's rest. The bloody message may also carry valuable or misleading information at the GM's discretion.

You can use a vial of astonishing ink to ask 5 questions before it's used up.

**Source:** `= this.source` (`= this.source-type`)
