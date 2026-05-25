---
type: deity
source-type: "Remaster"
domains: "Darkness, Death, Destruction, Moon"
favored-weapon: "Macuahuitl"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 3: [[Moth'S Supper]], Rank 5: [[Moon Frenzy]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Also known as the Destroyer, Lord of Night and Fear, and the Twisting Skull, Ah Pook is a cruel and cunning deity who has reveled in the suffering of mortals for as long as anyone can remember. However, rare is the occasion when the Destroyer causes direct harm to his victims. Instead, he relishes in misleading them, offering them apparent relief from their problems and concerns while inflaming their fears and insecurities, prompting them to act in ways that cause them to fall into a downward spiral of self-destruction. Ah Pook never forces someone to take a particular course of action, for their misery is more sublime if they brought it upon themselves.

**Title** The Destroyer

**Areas of Concern** death, destruction, the moon

**Edicts** nurture the fears and doubts of others, withhold your true intentions, make others realize the weight of their acts

**Anathema** guide others to overcome their fears and insecurities, provide swift relief to the suffering of others, save someone from a cruel fate brought about by their own hand

**Religious Symbol** skull with a crescent eclipse

**Sacred Animal** maggot

**Sacred Colors** black, white, gold

**Source:** `= this.source` (`= this.source-type`)
