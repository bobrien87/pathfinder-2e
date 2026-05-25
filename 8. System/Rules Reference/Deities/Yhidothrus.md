---
type: deity
source-type: "Remaster"
domains: "Death, Decay, Fate, Time"
favored-weapon: "Spiked-chain"
divine-font: "Harm"
divine-skill: "Society"
divine-spells: "Rank 1: [[Déjà Vu]], Rank 4: [[Morass Of Ages]], Rank 6: [[Cast Into Time]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Yhidothrus is the demon lord of the horrific aspects of time: erosion, decay, entropy, the fear of aging, and worms. The Ravager Worm operates slowly, letting time do his work, as his twisting body grows ever longer. Rumored to be connected (physically and in origin) to qlippoths, Yhidothrus's form is an infinitely long worm with night black flesh and a mouth of a dozen jaws and countless teeth. This demon lord's physical connection to the realm of qlippoths can also explain his slow workings; he is physically incapable of reaching into the territory of the other demon lords. His cults tend to be solitary individuals determined to avoid death and aging, transforming themselves into liches or other monstrosities, doing the demon lord's work less for his power and more to avoid his reach, letting him decay other things in exchange for preserving their existence.

**Title** The Ravager Worm

**Areas of Concern** Age, entropy, time, worms

**Edicts** Advance the destruction of all things, extend your life by any means necessary, sow discord among civilizations

**Anathema** Act rashly without careful planning, promote the creation of a place, thing, or idea

**Religious Symbol** worm-filled hourglass

**Sacred Animal** worm

**Sacred Colors** black, pale yellow

**Source:** `= this.source` (`= this.source-type`)
