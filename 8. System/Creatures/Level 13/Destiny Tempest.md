---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Destiny Tempest"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Air"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Greater Darkvision]]"
languages: "Sussuran (cant speak any language, Telepathy 100, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +21, Deception +26, Stealth +27"
abilityMods: ["+4", "+8", "+6", "+8", "+7", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Sound Without Voice"
    desc: "A creature damaged by the destiny tempest's slithering whisper Strike must succeed at a DC 33 [[Will]] save or become [[Frightened]] 2."
  - name: "Swiftness"
    desc: "A destiny tempest's movement doesn't trigger reactions."
armorclass:
  - name: AC
    desc: "34; **Fort** +19, **Ref** +24, **Will** +26"
health:
  - name: HP
    desc: "230; **Immunities** bleed, paralyzed, poison, sleep; **Weaknesses** force 10, spirit 10"
abilities_mid:
  - name: "Center of Destiny"
    desc: "`pf2:r` **Trigger** A creature within 30 feet benefits from a fortune effect <br>  <br> **Effect** Shadows surround and steal away the destiny tempest, who reappears in an open space adjacent to the triggering creature."
  - name: "Ebbing Cloud"
    desc: "15 feet. Destiny tempests surround themselves with thoughts of averted fates, creating a thick metaphysical soup that cloys the mind and clouds ambition. Creatures in the area moving toward the destiny tempest treat the area as difficult terrain."
  - name: "No Breath"
    desc: "Destiny tempests do not need to breathe."
  - name: "Unspeakable Insights"
    desc: "Touching a destiny tempest's mind even briefly grants a powerful and painful awareness of uncharted pasts, presents, and futures, too impossibly vast for mortal minds to conceptualize or contain. Whenever a creature targets the destiny tempest with a magical mental effect, it must attempt a DC 33 [[Will]] save. <br> - **Critical Success** The creature is unaffected and becomes immune to unspeakable insights for 24 hours. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature takes 3d6 mental damage. <br> - **Critical Failure** The creature takes 6d6 mental damage and becomes [[Confused]] for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Slithering Whisper +25 (`pf2:1`) (air, finesse, magical), **Damage** 2d8+10 bludgeoning plus 1d8 mental plus [[Sound Without Voice]]"
  - name: "Ranged strike"
    desc: "Umbral Breath +25 (`pf2:1`) (air, void, range 30 ft.), **Damage** 4d10 void"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33, attack +25<br>**6th** [[Never Mind]]<br>**5th** [[Subconscious Suggestion]], [[Truespeech]] (Constant)<br>**2nd** [[Darkness]]<br>**1st** [[Detect Magic]], [[Figment]]"
abilities_bot:
  - name: "Divergent Potential"
    desc: "`pf2:2` The destiny tempest chooses two creatures it can see within 60 feet and rolls two slithering whisper Strikes, one against each creature. After seeing the outcomes of the two Strikes, the destiny tempest chooses one of the two targets to pursue, Flies up to 60 feet to reach the chosen target, and uses the result of the chosen Strike; the other Strike is lost. If the destiny tempest is prevented from reaching its chosen target, the attack is prevented and the chosen Strike is lost."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Before the Jaathoom Empire, the Plane of Air was ruled by destiny tempests from their Reverient Empire of Lost Nights. When the jaathoom armies crushed the Reverient Empire, they trapped the defeated destiny tempests in bronze spheres scattered across the Plane of Air, prisons of time and everlasting nightmare.

```statblock
creature: "Destiny Tempest"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
