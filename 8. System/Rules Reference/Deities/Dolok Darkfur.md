---
type: deity
source-type: "Remaster"
domains: "Family, Knowledge, Might, Nature"
favored-weapon: "Claw, War-gavel"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Ant Haul]], Rank 2: [[Enlarge]], Rank 5: [[Moon Frenzy]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Perhaps the most well-known and active of the Sarkorian deities, Dolok Darkfur is immensely old, possessed of nearly unmatched physical prowess, and is an active participant in battles to reclaim Sarkoris from the demonic remnants of the Worldwound.

Dolok and his people, the Farheavens, fled to Iobaria following the Worldwound's opening, and Dolok kept the Farheavens safe for many generations until his last god caller died during a period where Dolok had slipped into a depressive hibernation. The loss of his last true mortal contact only deepened Dolok's depression, and he may have been lost to history forever had a group of archaeologists from the Pathfinder Society not sought out the Farheavens as part of a research project seeking out displaced Sarkorians.

Upon learning of Dolok's existence, the Pathfinders reunited him with the Farheavens leader, Nelket, a young woman with the ability to become a god caller.

Since Dolok and Nelket's bonding, the Farheavens clan has adopted a goblin tribe known as the Dragondwellers into their ranks. The combined might of Dolok, the Farheavens, and the Dragondwellers has made them one of the premier forces of reclamation in the Sarkoris Scar, both in combating demons directly and in sharing Dolok's ancient knowledge to restore Sarkorian society.

**Title** Champion of the Farheavens

**Areas of Concern** Guardians, family, preservation of culture

**Edicts** Protect the weak, pass your knowledge on to future generations, defend Sarkoris

**Anathema** Ally with demons, harm a member of the Farheavens Clan except in delivering fair justice

**Religious Symbol** bear paw print crossed by a bright red feather

**Sacred Animal** bear

**Sacred Colors** black, red

**Source:** `= this.source` (`= this.source-type`)
