---
type: deity
source-type: "Remaster"
domains: "Duty, Family, Protection, Repose"
favored-weapon: "Claw, Kukri"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Gentle Landing]], Rank 2: [[Disguise Magic]], Rank 7: [[Planar Palace]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Legend holds that the amurruns-known as catfolk to others-were created as guardians against threats to home, nature, and the world at large. While the goddess Adanye is not considered to be their creator, she is said to have mentored these first guardians, teaching them the skills necessary to protect and defend, both in combat and in careful interaction with others. She also taught the importance of what they protected, identifying the hearth and the home, as well as the right to self-determination and to solitude, as worthy of defense. She is said to have instilled in the amurruns their need for solitude and their esteem of imagination. A master teacher, she is depicted as a graying catfolk woman or a cat by the hearth fire, her large, gentle eyes full of wisdom.

**Title** The Warmth of the Hearth

**Areas of Concern** Hearth, imagination, protection, solitude

**Edicts** Keep your counsel, follow your heart, appreciate a warm hearth, defend those who welcome you into their home

**Anathema** Force anyone into drudgery or mindless work, deny support to loved ones, surrender when escape is an option, destroy a place that has given you shelter

**Religious Symbol** burning paw

**Sacred Animal** cat

**Sacred Colors** red, gold

**Source:** `= this.source` (`= this.source-type`)
