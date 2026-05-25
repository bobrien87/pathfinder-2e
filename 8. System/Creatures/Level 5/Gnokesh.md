---
type: creature
group: ["Archon", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gnokesh"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Chthonian, Diabolic, Draconic, Empyrean, Fey, Sakvroth, Shadowtongue, Utopian (Truespeech)"
skills:
  - name: Skills
    desc: "Arcana +12, Diplomacy +11, Nature +11, Occultism +12, Religion +13, Society +12, Lore (any one) +16"
abilityMods: ["+2", "+4", "+0", "+5", "+4", "+4"]
abilities_top:
  - name: "Light of Diligence"
    desc: "The gnokesh has devoted themselves to the thorough study of one particular Lore skill (with the bonus found in the Skills section), such as Heaven Lore or Warfare Lore. If the gnokesh rolls a critical failure to [[Recall Knowledge]] with this skill, they get a failure instead. They can also use the Aid action for this skill without frst preparing to help, and they automatically grant a +3 circumstance bonus."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +12, **Will** +15"
health:
  - name: HP
    desc: "70; **Immunities** fear effects; **Weaknesses** unholy 5"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Archon's Protection"
    desc: "`pf2:r` **Trigger** An enemy damages the archon's ally and both are within 15 feet of the archon <br>  <br> **Effect** The ally gains resistance 5 to all damage against the triggering damage, and the archon can make a Strike against the enemy. <br>  <br> > [!danger] Effect: Archon's Protection"
  - name: "Light of Diligence"
    desc: "`pf2:r` **Trigger** A willing ally within 15 feet critically fails at a check <br>  <br> **Effect** The ally gets a failure instead and becomes immune to Light of Diligence for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tome +13 (`pf2:1`) (divine, finesse, holy), **Damage** 1d6+6 bludgeoning plus 1d6 spirit"
  - name: "Ranged strike"
    desc: "Light Ray +13 (`pf2:1`) (divine, holy, light, magical, spirit, range 20 ft.), **Damage** 2d6 fire plus 2d6 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 22, attack +14<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Clairvoyance]], [[Translocate]] (At Will)<br>**3rd** [[Clairaudience]]<br>**2nd** [[Calm]], [[Silence]]<br>**1st** [[Light]], [[Message]], [[Sure Strike]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Alluring Knowledge"
    desc: "`pf2:2` **Frequency** once per hour <br>  <br> **Effect** A twisting scroll of runes made of light appears in an unoccupied square within 60 feet. Each creature adjacent to the runes must succeed at a DC 22 [[Will]] save or take 3d8 mental damage and be [[Fascinated]] with the magical text as long as it remains. The magical text lasts until the end of the gnokesh's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The structure of a gnokesh, a wheel of ancient tomes, refects its role in Heaven. These archons perfectly embody Heavenly knowledge, in particular the diligent pursuit of study and research. Each gnokesh is dedicated to one particular subject. This subject is crucial to their identity in a way few other than gnokeshes can understand. These archons avoid violence, fnding the pursuit of knowledge far more interesting. They prefer to gather with others of their kind in great libraries or serve as record-keepers or tutors for archivists, researchers, generals, advisors, and others who can use their expertise.

```statblock
creature: "Gnokesh"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
