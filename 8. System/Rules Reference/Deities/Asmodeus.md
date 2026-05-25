---
type: deity
source-type: "Remaster"
domains: "Confidence, Fire, Trickery, Tyranny"
favored-weapon: "Mace"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Charm]], Rank 4: [[Suggestion]], Rank 6: [[Mislead]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The many titles of Asmodeus—the Dark Prince, the First, the Lord of Darkness and Law to name a few—suit this ruler of Hell. The God-Fiend's concerns include contracts, tyranny, pride, and oppression. He maintains that a supreme order exists with him at the top, so he strives to bend mortal souls to eventually bring them all under his sway. When people believe they deserve power and wealth, and are willing to undertake any means to acquire them, one of Asmodeus's devils will be there to broker a deal that leads to that mortal's damnation.

**Title** The Prince of Darkness

**Areas of Concern** contracts, oppression, pride, tyranny

**Edicts** negotiate contracts to your best advantage, rule tyrannically and torture weaker beings, show subservience to your betters

**Anathema** break a contract, share power with the weak, insult Asmodeus by showing mercy to your enemies

**Religious Symbol** red pentagram

**Sacred Animal** serpent

**Sacred Colors** black, red

**Source:** `= this.source` (`= this.source-type`)
