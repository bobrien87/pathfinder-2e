---
type: deity
source-type: "Remaster"
domains: "Air, Ambition, Magic, Trickery"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Fleet Step]], Rank 2: [[Vomit Swarm]], Rank 6: [[Mislead]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Baalzebul was one of the first angels of Heaven, a glorious lieutenant who followed Asmodeus in his exodus to Hell. In this new realm, he led the infernal armies and trained several other archdevils as generals. When Asmodeus divided the nine realms of Hell between himself and the eight archdevils, Baalzebul protested, thinking he had earned a place at his god's side. Asmodeus responded by stripping away the archdevil's radiant form, reducing him to a figure composed of swarming flies. Now known as the Lord of Flies, he rules over Cocytus, the frozen seventh layer of Hell, and attracts followers possessed of deep ambition and a powerful drive to triumph.

**Title** Lord of Flies

**Areas of Concern** Arrogance, flies, lies

**Edicts** Convey yourself with regal dignity, claim what you desire and deserve, seek vengeance on those who wrong you

**Anathema** Provoke Baalzebul's envy, show humility

**Religious Symbol** iron crown and diamond

**Sacred Animal** fly

**Sacred Colors** black, White

**Source:** `= this.source` (`= this.source-type`)
