---
type: deity
source-type: "Remaster"
domains: "Destruction, Delirium, Repose, Sorrow"
favored-weapon: "Whip"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Charm]], Rank 3: [[Enthrall]], Rank 5: [[Wave Of Despair]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ozranvial is one's dearest friend until she isn't. The sahkil tormentor of despair and sadism isn't satiated by physical pain. Instead, she takes great pleasure in inserting herself into someone's life and pulling it apart until they are utterly broken by her machinations. The intimacy of a relationship makes its destruction all the more beautiful. Ozranvial will foster a relationship over years and even decades to enjoy the devastating outcome of her cruelty. She rules over the restless spirits created from the emotional damage she inflicts, tormenting them even after death.

**Title** Despair's Smile

**Areas of Concern** Despair, restless spirits, sadism

**Edicts** Be amicable until the time is right to strike, give false hope to all, make the choice that will cause more pain

**Anathema** Apologize sincerely for your actions, show emotional vulnerability

**Religious Symbol** teardrop with a malevolent grin

**Sacred Animal** hyena

**Sacred Colors** orange, yellow

**Source:** `= this.source` (`= this.source-type`)
