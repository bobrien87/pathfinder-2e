---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Champion]]", "[[Cleric]]"]
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your faith in your deity is represented in an extremely unusual way that some might call heretical. When you select this feat, you should detail the fundamental tenets of your splinter faith, though it shouldn't affect the deity's edicts or anathema. Choose four domains. These domains must be chosen from among your deity's domains, your deity's alternate domains, and up to one domain that isn't on either list and isn't anathematic to your deity. Any domain spell you cast from a domain that isn't on either of your deity's lists is always heightened to 1 rank lower than usual for a focus spell. For the purpose of abilities that depend on your deity's domains, the four domains you chose are your deity's domains, and any of your deity's domains you didn't choose are now among your deity's alternate domains.

**Special** Unless you take this feat at 1st level, changing the way you relate to your deity requires retraining, as described in the Changing Faith section below. If you take this feat and previously benefited from any effect that requires a domain your splinter faith doesn't include, such as a domain spell from Domain Initiate, you lose that effect.

At the GM's discretion, you can take this feat with other classes or archetypes that gain access to domains through a deity.

**Source:** `= this.source` (`= this.source-type`)
