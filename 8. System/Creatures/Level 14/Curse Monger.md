---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Curse Monger"
level: "14"
rare_01: "Rare"
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
    desc: "+23"
languages: "Aklo, Chthonian, Common, Daemonic, Fey"
skills:
  - name: Skills
    desc: "Arcana +25, Deception +25, Intimidation +23, Occultism +29, Stealth +24"
abilityMods: ["+1", "+5", "+3", "+8", "+4", "+4"]
abilities_top:
  - name: "Incurable Curse"
    desc: "The curse monger is permanently [[Clumsy]] 1, [[Drained]] 1, [[Enfeebled]] 1, or [[Stupefied 1]] by a curse that can't be removed from them in any way. The GM chooses the condition and decides whether the curse is arcane, divine, occult, or primal."
armorclass:
  - name: AC
    desc: "35; **Fort** +23, **Ref** +25, **Will** +26"
health:
  - name: HP
    desc: "230"
abilities_mid:
  - name: "–2 To All Saves vs. Curses"
    desc: ""
  - name: "Cursed Aura"
    desc: "30 feet. The very earth and air around the curse monger are poisoned by the curses that burden their soul. Any creature who enters or starts their turn in the aura must succeed at a DC 31 [[Will]] save or be [[Doomed]] 1 (or [[Doomed]] 2 on a critical failure). Regardless of the result of its save, the creature is then temporarily immune for 1 hour."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sickle +25 (`pf2:1`) (agile, finesse, magical, trip), **Damage** 1d6 bleed plus 2d4+13 slashing"
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+13 bludgeoning"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 37, attack +29<br>**7th** (3 slots) [[Possession]]<br>**6th** (3 slots) [[Cursed Metamorphosis]], [[Dominate]], [[Never Mind]], [[Phantasmal Calamity]], [[Spellwrack]]<br>**5th** (3 slots) [[False Vision]], [[Mariner's Curse]], [[Wave of Despair]]<br>**4th** (3 slots) [[Outcast's Curse]], [[Vision of Death]]<br>**3rd** (3 slots) [[Hypercognition]], [[Mind Reading]], [[Slow]]<br>**2nd** (3 slots) [[Blood Vendetta]], [[Darkness]], [[Laughing Fit]], [[Paranoia]]<br>**1st** (3 slots) [[Bane]], [[Daze]], [[Fear]], [[Figment]], [[Ill Omen]], [[Message]], [[Telekinetic Hand]], [[Void Warp]]"
abilities_bot:
  - name: "Share Burden"
    desc: "`pf2:1` The curse monger shares their awful burden with one creature they can see within 120 feet. The target must succeed at a DC 37 [[Will]] save or be afflicted with the same condition as the curse monger's incurable curse for 24 hours. On a critical failure, the curse's value is 2. The curse lasts for 24 hours but can be removed (unlike the incurable curse), and ends if the curse monger dies. This action has the same tradition trait as incurable curse."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Oracles who have been consumed by their visions and the divine gifts bestowed upon them turn to more sinister paths, becoming curse mongers. Seeking to rid themselves of the shadows that haunt them, curse mongers lash out and attempt to bind others to their fate.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Curse Monger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
