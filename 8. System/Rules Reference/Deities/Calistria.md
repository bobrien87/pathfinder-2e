---
type: deity
source-type: "Remaster"
domains: "Pain, Passion, Secrecy, Trickery"
favored-weapon: "Whip"
divine-font: "Harm, Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Charm]], Rank 3: [[Enthrall]], Rank 6: [[Mislead]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Calistria is as sharp as the three daggers of her holy symbol, ever ready with a quick quip or backhanded compliment. She is the god of lust, trickery, and revenge. She considers herself above the arbitrary moral and societal sensibilities of mortals, and she encourages her followers to act the same. Though Calistria isn't exclusively an elven deity, she is among the most widespread of elven gods and attracts followers from all over Golarion.

Trickery is one of Calistria's concerns, but her schemes far surpass the designation of mere pranks or pettiness. At first, Calistria's vengeance resembles kindness and even generosity as she leads the transgressor into false happiness with pleasant events and good fortune. Only once it's too late does Calistria reveal herself as the architect of the culprit's doom and shatters their idyllic life.

**Title** The Savored Sting

**Areas of Concern** lust, revenge, trickery

**Edicts** pursue your personal freedom, seek hedonistic thrills, take revenge

**Anathema** become too consumed by love or a need for revenge, let a slight go unanswered

**Religious Symbol** three daggers

**Sacred Animal** wasp

**Sacred Colors** black, yellow

**Source:** `= this.source` (`= this.source-type`)
