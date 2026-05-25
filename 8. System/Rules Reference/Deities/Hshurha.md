---
type: deity
source-type: "Remaster"
domains: "Air, Cold, Destruction, Dust"
favored-weapon: "Longbow"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Gust Of Wind]], Rank 2: [[Summon Elemental]], Rank 4: [[Vapor Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Hshurha, Duchess of All Winds, is the elemental lord of air, last breaths, and windstorms. She rules the Plane of Air from her translucent palace, Verglas Precessional, surrounded by her court of air elementals, planar dignitaries, and favored guests. The Duchess is naturally [[Invisible]], and her true form—if she even has such a thing—is a mystery. Cruel and tyrannical, Hshurha enjoys toying with outsiders in her realm, and she is known to be especially vicious toward creatures with solid forms. She creates and destroys magnificent ice and dust sculptures according to her tumultuous whims, and her machinations often seem convoluted and nonsensical, even to her inner circle. Most on the plane both respect and fear her.

**Title** Duchess of All Winds

**Areas of Concern** Air, last breaths, windstorms

**Edicts** Revel in formlessness and freedom, humiliate terrestrial creatures, kill foes via falling or hazards from high winds

**Anathema** Deny a flying creature the ability to fly, walk on earth if you could easily travel otherwise

**Religious Symbol** lightning vortex around eye

**Sacred Animal** roc

**Sacred Colors** white, yellow

**Source:** `= this.source` (`= this.source-type`)
