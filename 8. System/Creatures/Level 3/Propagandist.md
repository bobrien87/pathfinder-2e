---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Propagandist"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10"
languages: "Common"
skills:
  - name: Skills
    desc: "Diplomacy +11, Performance +10, Society +10, Legal Lore +8"
abilityMods: ["+0", "+2", "+1", "+1", "+3", "+4"]
abilities_top:
  - name: "+2 to Sense Motive"
    desc: ""
  - name: "Nuanced Spin"
    desc: "The propagandist phrases everything loosely and vaguely enough that, though it's always misleading, none of it is false. The propagandist can use Diplomacy instead of Deception to [[Create a Diversion]] or `act feint statistic=diplomacy`, and instead of Intimidation to `act coerce statistic=diplomacy`. A creature attempting to [[Sense Motive]] against the propagandist gets a result one degree of success worse than they rolled."
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +9, **Will** +12"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Shortsword +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+4 piercing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 21, attack +13<br>**2nd** (2 slots) [[Blistering Invective]], [[Paranoia]]<br>**1st** (3 slots) [[Bullhorn]], [[Concordant Choir]], [[Detect Magic]], [[Fear]], [[Haunting Hymn]], [[Message]], [[Sanctuary]], [[Summon Instrument]]"
  - name: "Bard Composition Spells"
    desc: "DC 21, attack +13<br>**2nd** [[Rallying Anthem]]<br>**1st** [[Courageous Anthem]], [[Hymn of Healing]], [[Lingering Composition]]"
abilities_bot:
  - name: "No Hard Feelings"
    desc: "`pf2:2` The propagandist offers amnesty and other benefits to all who choose to join them. All enemies who can hear the propagandist must attempt a DC 19 [[Will]] save. If any of the propagandist's allies is currently benefiting from one of the propagandist's bard composition spells, any enemy who is aware of that takes a –2 circumstance penalty to the save. <br> - **Critical Success** The creature sees through the propagandist's pitch and is temporarily immune for 24 hours. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature's conviction stumbles. Until the end of its next turn, the creature must succeed at a DC 5 flat check to target the propagandist with a hostile action. <br> - **Critical Failure** The creature finds the propagandist's offer too good to pass up, switching sides in the combat and instantly gaining any benefits the propagandist is currently granting their allies. At the end of each of its turns, the creature can attempt another DC 19 [[Will]] save to snap out of it and rejoin their allies."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The misleadings, half-facts, and effortless spin propagandists cast over events create proof of whatever their bosses need them to prove.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Propagandist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
