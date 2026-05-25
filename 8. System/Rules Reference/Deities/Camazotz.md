---
type: deity
source-type: "Remaster"
domains: "Abomination, Darkness, Indulgence, Trickery"
favored-weapon: "Javelin"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 3: [[Cup Of Dust]], Rank 5: [[Umbral Journey]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Camazotz began life as a vampire bat inhabiting the demiplane of Xibalba, but soon learned how to flit between planes and found himself in a cavernous realm within the Outer Rifts. After the demonic inhabitants there took notice of this visitor lurking in the shadows, they began to use Camazotz to send messages to their mortal followers. His payment came in the form of blood, and his eagerness to accept this renumeration from within the chthonian gloom earned him the sobriquet "The Hungry Dark." His journeys took him to the Land of the Eleven Deaths, a Darklands realm beneath Arcadia, where he feasted on more blood. His feedings eventually elevated him to godhood as the Lord of Stolen Blood. Camazotz remains on the move, splitting his time between the House of the Bat in Xibalba, the Outer Rift caves of Argahoz, and the Land of the Eleven Deaths. With no one true domain to call home, Camazotz has more freedom to roam than most other gods, allowing him to indulge his thirst wherever he pleases.

**Title** Lord of Stolen Blood

**Areas Of Concern** bats, blood, caverns, nocturnal predators

**Edicts** slake your thirst with blood, stalk prey from the shadows, subvert the trappings and comforts of civilization

**Anathema** do reckless harm to bats, spill blood without reason

**Religious Symbol** bat-shaped rune

**Sacred Animal** vampire bat

**Sacred Colors** black, red

**Source:** `= this.source` (`= this.source-type`)
