---
type: deity
source-type: "Remaster"
domains: "Destruction, Fire, Sun, Zeal"
favored-weapon: "Scimitar"
divine-font: "Harm, Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 4: [[Wall Of Fire]], Rank 7: [[Volcanic Eruption]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Fire burns, but it also provides light in the darkness, warms the cold, and cooks food for the hungry. Those who understand the primordial power of fire might worship the Plane of Fire and related spirits as a single divine covenant. Usually unbound by the stricter moralities of most other faiths, followers of the Light of the Everlasting Flame might be chaotic arsonists burning down everything they see or beacons of hope for the lost. In either case, they always bring a heart full of passion to every endeavor. While there are plenty of these faithful in the hot, sunny places of the world, they can also be found in colder or darker climates, where their devotion to flames is needed the most.

**Covenant Members** fire elementals, ifrits, phoenixes, the Plane of Fire, spirits of fire

**Areas of Concern** ash, fire, intensity, light, smoke

**Edicts** carry a light source at all times, express your wrath through smoke and flame, warm those who are cold

**Anathema** cover or extinguish a flame without reason, languish in the darkness for no reason

**Religious Symbol** twisting flame

**Source:** `= this.source` (`= this.source-type`)
