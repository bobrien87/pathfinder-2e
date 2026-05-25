---
type: deity
source-type: "Remaster"
domains: "Duty, Fire, Nature, Perfection"
favored-weapon: "Trident"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Plant Or Fungus]], Rank 3: [[Fireball]], Rank 5: [[Plant Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Orange poppies arranged in a flame on a green field grace the Knight of Laurels's standard. His laurels and wreaths are a heavy collection of favors asked and given by the cherished of each court defeated on his decennial campaign across the plane. His appearance is that of an enormous centaur covered in dark armor made of hardened, thorny vines. His immortal host, champions who damned their souls in the name of obligation and who know the true meaning of sacrifice, ride to the end of days in the Hanging Marches. Knights who will win at any cost, foresters who will burn the copse and all its life within to nourish regrowth, and physicians who will administer medicine that has equal chance of killing: those who will pay the highest prices salute Furcas.

**Title** The Knight of Laurels

**Areas of Concern** Duty, flames, herbalism

**Edicts** Duel with others, dine with your opponents before fighting, bask in the sun

**Anathema** Break dueling etiquette, waste medicine on lost causes, accept convenience over perfection

**Religious Symbol** flaming pitchfork

**Sacred Animal** snake

**Sacred Colors** red, yellow

**Source:** `= this.source` (`= this.source-type`)
