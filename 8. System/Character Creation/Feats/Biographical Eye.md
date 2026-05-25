---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]", "[[Secret]]", "[[Skill]]"]
prerequisites: "master in Society"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

In even a brief conversation or social interaction, you pick up on subtle social and visual cues to learn a great deal about a person's origin and history. You might notice bits of green under the person's fingernails and determine they're an herbalist, spy a pin indicating their membership in a secret society, or something similar. You pick up on only details that have to do with their societal role, so you might learn the city district where a vampire lives, but wouldn't learn any of their weaknesses, nor necessarily even that they are a vampire. Spend 1 minute in the presence of someone you haven't met before, or haven't met since you first gained Biographical Eye, then attempt a DC 30 [[Society]] check. You gain a +1 circumstance bonus to the check if you engaged the person in conversation during this time. If the person is deliberately trying to conceal their nature or present a false identity, you learn about their false biography rather than their true one unless the result of your Society check exceeds their Will DC.
- **Critical Success** You learn the creature's profession, their specialty within that profession, and a major accomplishment or controversy from their career. You also learn the nation and settlement where they live, as well as the district in a city large enough to have districts. In addition, you learn the nation or settlement where they spent their formative years.
- **Success** You learn the creature's profession and specialty within that profession. You learn the nation or settlement where they normally live.
- **Failure** You learn the creature's profession and the region of the world they hail from, but no more.
- **Critical Failure** You learn a piece of erroneous information about the creature.

**Source:** `= this.source` (`= this.source-type`)
