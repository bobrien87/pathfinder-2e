---
type: deity
source-type: "Remaster"
domains: "Change, Healing, Nature, Truth"
favored-weapon: "Katana"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Thunderstrike]], Rank 3: [[Animal Vision]], Rank 6: [[Tree Of Seasons]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Before he was a god, Baekho was a tiger who protected the forests of Tian Xia. Once, when he was gravely injured, he sheltered under the branches of a persimmon tree. As he experienced the changing of seasons beneath the tree's branches, an innate understanding of the world stirred within him. He awakened as a divine spirit with a human form with white hair, black-tipped white tiger ears, and deep blue tiger eyes. In his feline form, the fur that had once been an inferno of orange became a blinding white. His religious symbol, a snow-tipped persimmon branch laden with vibrant red-orange fruit, represents his awakening as a divine spirit who cherishes harmony.

**Title** The Lord of the Seasons

**Areas of Concern** Balance, healing, nature, seasons

**Edicts** Bridge rifts between allies, embrace change, consider all sides of a disagreement before passing judgment

**Anathema** Allow bias to guide your judgment, reject change in favor of stagnation, sow discord between allies, take more than you give

**Religious Symbol** persimmon branch against the sun

**Sacred Animal** tiger

**Sacred Colors** orange, white

**Source:** `= this.source` (`= this.source-type`)
