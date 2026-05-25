---
type: deity
source-type: "Remaster"
domains: "Void, Perfection, Protection, Travel"
favored-weapon: "Shield-spikes"
divine-font: "Harm, Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Interposing Earth]], Rank 4: [[Containment]], Rank 5: [[Magic Passage]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Universe as it currently exists depends on strict boundaries, the separation of reality into distinct matter instead of primordial chaos. The planes are likewise divided from each other by metaphysical borders, pierced by only portals and planar rifts. Dramindyr, the Skin of Creation, is the first arbitrator who forms these perimeters; their very body is the membrane that holds every plant, animal, mineral, and dimension separate from one another. To cross between planes is to walk along Dramindyr's spine, and to rip holes in the planar fabric is to pierce Dramindyr's infinite coils. Indeed, the presence of the Worldwound on Golarion was an open sore on Dramindyr's side for over a century, and its closure may have caused Dramindyr to return more of their attention to their rare adherents upon Golarion.

**Title** The Skin of Creation

**Areas of Concern** Borders, physical integrity, the planes, separation

**Edicts** Create and maintain clear physical boundaries, repair planar tears, banish summoned creatures

**Anathema** Merge a creature with another, cause a planar rift, strand a creature in a different plane than it belongs

**Religious Symbol** infinite looping coils

**Sacred Animal** siphonophore

**Sacred Colors** blue, green

**Source:** `= this.source` (`= this.source-type`)
