---
type: deity
source-type: "Remaster"
domains: "Confidence, Glyph, Knowledge, Truth"
favored-weapon: "Dagger"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Mindlink]], Rank 2: [[Embed Message]], Rank 3: [[Enthrall]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Heart-Speaker Eritrice represents honest debate, opinions, and truth. Facts and information are important to Eritrice, but truths and wisdom gained through discussion are far more valuable to her than those gained through books. She maintains there is nothing wrong with disagreeing so long as the disagreement is respectful, and that it is crucial to be open to discussion, willing to consider new information, and receptive to forming new opinions. Opinions are valuable in that they help understand other views, but Eritrice reminds her followers that opinions are not facts and can be incorrect and even harmful. When lies are spoken or become the rule of the land, those that follow Eritrice work through networks of like-minded individuals to spread the truth using messages sent to all who will listen.

**Title** Heart-Speaker

**Areas of Concern** Debate, opinions, truth

**Edicts** Spread truth, debate contentious issues, aid messengers

**Anathema** Sow or perpetuate lies, obstruct discussion, argue in bad faith

**Religious Symbol** lion-shaped lectern

**Sacred Animal** lion

**Sacred Colors** gold, white

**Source:** `= this.source` (`= this.source-type`)
