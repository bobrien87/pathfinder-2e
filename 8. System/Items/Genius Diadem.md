---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Apex]]", "[[Arcane]]", "[[Intelligent]]"]
price: "{'gp': 24000}"
usage: "worncirclet"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +22; precise vision 30 feet, imprecise hearing 30 feet, constant *detect magic*

**Communication** speech (Common, Draconic, and eight other common languages)

**Skills** Arcana +34, seven Lore skills +28, Occultism +28, Society +28

**Int** +8, **Wis** +0, **Cha** +4

**Will** +24

The *genius diadem* is a *[[Crown of Intellect]]* that typically acts like an arrogant professor or mentor, often boasting that it is a certified greater intellect and far superior to your own intelligence, even after the benefits the diadem grants you. The *genius diadem* encourages you to learn things for yourself rather than actually attempting to Recall Knowledge for you, though you or your allies might be able to play on its arrogance using Deception to trick it into doing so. In addition to allowing you to activate it, the diadem can use the Search Your Mind activation with its own actions, though if it does so, the diadem gains the benefits instead of you. Only the diadem can use the following activation.

**Activate—Brain Drain** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Effect** The *genius diadem* casts 7th-rank [[Never Mind]].

**Source:** `= this.source` (`= this.source-type`)
