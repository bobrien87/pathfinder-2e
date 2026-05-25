---
type: deity
source-type: "Remaster"
domains: "Ambition, Change, Might, Toil"
favored-weapon: "Sansetsukon"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Jump]], Rank 3: [[Feet To Fins]], Rank 4: [[Hydraulic Torrent]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Once a humble carp, Jin Li is the god of the determined and the hardworking. Just as he worked day after day to successfully jump a waterfall and ascend to godhood, he guides those who look to improve themselves and face challenges head-on. For Jin Li, there is no success without hard work, tenacity, and a little bit of luck. Failure and weakness are not something to be ashamed of, but rather opportunities to learn and grow. Success is also not a one-time thing for Jin Li, and once he has achieved one goal, he soon sets his eyes on another. The road to self-improvement doesn't end with godhood, after all.

**Title** The Golden Dragon Carp

**Areas of Concern** Challenges, dares, promotions, self-improvement

**Edicts** Take up dares and challenges in good faith, persist with creativity and tenacity, own up to your failures as a way to improve oneself

**Anathema** Give up without trying, dismiss or mock someone's effort, take success for granted, discount the power of beginner's luck or luck in general

**Religious Symbol** dragon carp jumping a waterfall

**Sacred Animal** carp

**Sacred Colors** blue, gold

**Source:** `= this.source` (`= this.source-type`)
