---
type: deity
source-type: "Remaster"
domains: "Darkness, Protection, Repose, Vigil"
favored-weapon: "Shortbow"
divine-font: "Harm, Heal"
divine-skill: "Religion"
divine-spells: "Rank 1: [[Sleep]], Rank 4: [[Mountain Resilience]], Rank 7: [[Momentary Recovery]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Mortals have always needed ways to remember and honor their ancestors, and it was from this fundamental need the psychopomp usher Vavaalrav first imagined the spires and steeples of the Boneyard. Vavaalrav is the guardian of sacred places, and the chill of his breath and stillness of his presence is felt across every mausoleum, tomb, and other burial ground of the Universe. The Steeple's Skull does not tolerate when the sanctity of a holy site or the rest of the dead is disturbed, and his symbol is used by mortals to ward graves against foul spirits and grave robbers alike.

**Title** The Steeple's Skull

**Areas of Concern** Gargoyles, holy ground, rest

**Edicts** Create and erect grave markers, lay bodies to rest, protect graveyards and sacred grounds from despoilment and supernatural threats

**Anathema** Treat grave sites irreverently, allow others to despoil the dead or rob a grave, create undead, desecrate a corpse

**Religious Symbol** vertical line with a horizontal crossbar near the top and a circle around the overlap

**Sacred Animal** hound

**Sacred Colors** gray

**Source:** `= this.source` (`= this.source-type`)
