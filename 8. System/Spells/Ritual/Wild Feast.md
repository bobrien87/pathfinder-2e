---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
traits: ["[[Mythic]]"]
cast: "8 hours"
range: "centered on you"
area: "500-foot burst"
duration: "3 days"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You draw forth latent hostility in the local flora and fauna. Even domesticated animals might turn on their owners.
- **Critical Success** As success, except that animal companions, pets, familiars with the animal, fungus, or plant trait, and similar creatures (subject to the GM's discretion) are also initially affected. Each day for the duration, during daily preparations, its master must succeed at a [[Diplomacy]] check or [[Nature]] check against a DC equal to the ritual's casting DC or the creature temporarily loses the minion trait and can't be Commanded that day. The creature remains near its master but doesn't help them in any way.
- **Success** Carnivorous animals and plants in the area are automatically hostile toward humanoids and other natural enemies. Animal companions, pets, familiars with the animal, fungus, or plant trait, and similar creatures don't turn on their masters, but attempts to [[Command an Animal]] or to [[Demoralize]] any creatures with the animal, fungus, or plant trait take a –2 status penalty.
- **Failure** The ritual has no effect.
- **Critical Failure** A terrible hunger awakens within the casters. Each caster is permanently cursed to hunger for the taste of flesh of their own ancestry; this is identical to the ghoul's forbidden cravings curse, except the raw meat must be from a member of their own ancestry. The DC of this curse is equal to the ritual's casting DC.

**Heightened (+2)** Double the ritual's area.

**Source:** `= this.source` (`= this.source-type`)
