---
type: deity
source-type: "Remaster"
domains: "Cities, Creation, Wyrmkin, Toil"
favored-weapon: "Jaws, Light-hammer"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Object Reading]], Rank 5: [[Wave Of Despair]], Rank 9: [[Resplendent Mansion]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In the days of Old Koloran and Ninshabur, the name Gaasham was exalted in song, from the highest ziggurat to the lowliest homesteader's hearth. He was the muse on the wind who enkindled the hearts of architects and builders, promising them a path toward their grand works and opuses. Gaasham guided their chisels and accepted their praise, ever hopeful to craft a work which might withstand the doom that haunted him since the early days of creation.

Gaasham was conceived in the minds of Apsu and Sarshallatu for a role other than the one he would inherit. He clung within his shell too long, fearful of what would be asked of him, fearful of his finite form in the presence of beings so far grander than himself, and fearful of the fallibility that might see him shame his progenitors. Swaddled within his egg, he mistook the cacophonous sounds which rattled through his being as the thunderous songs of his mother, only to emerge to find the desolation inflicted by Dahak upon all of creation.

Apsu was the first to gaze upon his second laid (but late to hatch) son, and his eyes were filled with a stern pity. All Gaasham's fears coalesced and were promptly cast aside. He was granted the mantle of Architect, to serve as successor to his brother Dahak, now condemned to the role of destroyer. Gaasham embraced this new role and, with it, all the doom which is preordained to befall all usurpers. Gaasham would serve his father, and all that he would build would be consigned to ruin.

**Title** The Architect

**Areas of Concern** construction, self- actualization, legacies

**Edicts** build when it is asked of you, foster growth in others, meditate upon your actions

**Anathema** act without thinking, hesitate in the face of destructive forces, refuse to change your ways

**Religious Symbol** a bronze oval, half-oxidized

**Sacred Animal** draft lizard

**Sacred Colors** bronze, eggshell, teal

**Source:** `= this.source` (`= this.source-type`)
