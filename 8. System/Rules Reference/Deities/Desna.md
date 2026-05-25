---
type: deity
source-type: "Remaster"
domains: "Dreams, Luck, Moon, Travel"
favored-weapon: "Starknife"
divine-font: "Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Sleep]], Rank 4: [[Translocate]], Rank 5: [[Dreaming Potential]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Desna is one of the oldest goddesses, a divinity who predates mortal life, yet one who has come to adore it for its beauty, capacity for diversity, and pursuit of growth. According to legend, Desna placed the stars in the night sky of the Universe, an act that Sarenrae found so inspiring that she chose her favorite stars to become the suns of countless worlds. When mortal life rose on those worlds, Desna's first gift to them was a beacon of hope, for she made the first star and her home, Cynosure, the brightest in the sky, giving those on the countless worlds something to gaze upon, to use in navigation, and to inspire their dreams.

**Title** Song of the Spheres

**Areas of Concern** dreams, luck, stars, travelers

**Edicts** aid fellow travelers, explore new places, express yourself through art and song, find what life has to offer

**Anathema** foster despair or terror in the innocent, cast nightmare or use similar magic to corrupt dreams, engage in bigoted behavior

**Religious Symbol** butterfly

**Sacred Animal** butterfly

**Sacred Colors** blue, white

**Source:** `= this.source` (`= this.source-type`)
