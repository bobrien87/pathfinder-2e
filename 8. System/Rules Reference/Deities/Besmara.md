---
type: deity
source-type: "Remaster"
domains: "Destruction, Trickery, Water, Wealth"
favored-weapon: "Rapier"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 3: [[Feet To Fins]], Rank 5: [[Mariner'S Curse]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Besmara, the Pirate Queen, cuts a brash and bold figure, as she is often depicted wearing buccaneer apparel consisting of loose-fitting, eye-catching clothing and black boots, and her hair is wind-tossed on even the calmest day. She sails her divine ship Seawraith across the planes, staging raids on Hell, Heaven, and all places in between. Once nothing more than a powerful spirit of water with the ability to manipulate sea monsters, Besmara grew slowly in power over the centuries from sacrifices made by seafaring people. After defeating and consuming rival spirits of battle, gold, and wood, she became a minor god of piracy, strife, and sea monsters. She and her followers adhere to a simple code of greed: take what you desire, no matter who it might belong to. Despite this, Besmara and her worshippers are generally loyal to one another, knowing that while on the waves raiding ships for treasure, a pirate crew can survive only if its members trust one another.

**Title** The Pirate Queen

**Areas of Concern** piracy, sea monsters, strife

**Edicts** sail the seas, stay loyal to captain and crew, take what you want

**Anathema** betray shipmates, forsake piracy, settle on land

**Religious Symbol** skull and crossbones

**Sacred Animal** parrot

**Sacred Color** black, white

**Source:** `= this.source` (`= this.source-type`)
