---
type: deity
source-type: "Remaster"
domains: "Fate, Nature, Void, Star"
favored-weapon: "Bola"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Gravitational Pull]], Rank 3: [[Feet To Fins]], Rank 4: [[Variable Gravity]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Whether mortals realize it or not, the stars, moons, systems, and galaxies of the Universe all flow in accordance with ancient and fundamental laws set in motion at the dawn of creation. Though magic might pull them from their charted course, even this movement is guided by a force sewn into the fabric of the cosmos. Telastmar, the Cosmic Dyne, is the manifestation of these celestial orbits, keeping the Universe in constant movement. Because this turn of planets and moons controls the tides, Telastmar also holds sway over the oceans, though they curiously seem more concerned with the fish that live in such waters. Adherents claim that Telastmar is the lord and creator of all fish, guiding them on their migrations throughout rivers and seas.

**Title** The Cosmic Dyne

**Areas of Concern** Fish, gravity, orbits, planets

**Edicts** Aid natural migrations, chart the stars and tides, observe and calculate patterns, build orreries

**Anathema** Use a net, waste a fish, block out the stars with unnatural light

**Religious Symbol** fish forming a constellation

**Sacred Animal** humpback whale

**Sacred Colors** black, silver

**Source:** `= this.source` (`= this.source-type`)
