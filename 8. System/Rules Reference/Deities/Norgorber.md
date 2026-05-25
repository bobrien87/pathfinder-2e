---
type: deity
source-type: "Remaster"
domains: "Death, Secrecy, Trickery, Wealth"
favored-weapon: "Shortsword"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 2: [[Invisibility]], Rank 4: [[Vision Of Death]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

As befits a god of secrets, Norgorber's life before his ascension is a mystery, but his goals since assuming godhood are clear—to embolden those who use hidden or forbidden knowledge for domination, control, and personal gain. Norgorber does this work in many guises, each designed to build the faith of his followers as they work in the shadows—and help him to accomplish his own unknown and unknowable goals.

**Title** Blackfingers, Father Skinsaw, the Gray Master, the Reaper of Reputation

**Areas of Concern** greed, murder, poison, secrets

**Edicts** keep your true identity secret, sacrifice anyone necessary, take every advantage in a fight, work from the shadows

**Anathema** allow your true identity to be connected to your foul dealings, share a secret freely, show mercy

**Religious Symbol** one-eyed mask

**Sacred Animal** spider

**Sacred Colors** black, gray

**Source:** `= this.source` (`= this.source-type`)
