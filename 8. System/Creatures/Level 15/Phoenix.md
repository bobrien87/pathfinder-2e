---
type: creature
group: ["Beast", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Phoenix"
level: "15"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Fire"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Darkvision]]"
languages: "Common, Empyrean, Pyric, Sussuran"
skills:
  - name: Skills
    desc: "Acrobatics +30, Athletics +27, Diplomacy +31, Intimidation +27, Nature +25"
abilityMods: ["+6", "+7", "+5", "+7", "+6", "+6"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "36; **Fort** +27, **Ref** +31, **Will** +28"
health:
  - name: HP
    desc: "300; regeneration 20 (deactivated by cold or unholy), self-resurrection; **Immunities** fire; **Weaknesses** cold 10, unholy 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 20 (Deactivated by Cold or Unholy)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Self-Resurrection"
    desc: "When a phoenix dies, they collapse into a pile of smoldering ashes before returning to life fully healed 1d4 rounds later, as if subject to a 7th-rank [[Resurrect]] ritual. Self-resurrection happens only if there are some remains to resurrect; for instance, a phoenix killed by a [[Disintegrate]] spell can't use this ability. <br>  <br> A phoenix whose remains rest within an area devoted to an unholy deity by [[Consecrate]] can't self-resurrect until their remains are no longer in that area. A phoenix can self-resurrect only once per year."
  - name: "Shroud of Flame"
    desc: "20 feet. @Damage[4d6[fire]|options:area-damage], DC 37 [[Reflex]] save. <br>  <br> While this aura is active, any adjacent creature that hits the phoenix with a melee attack or otherwise touches them takes 2d6 fire damage. The phoenix can activate or deactivate the aura with a single action, which has the concentrate trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +30 (`pf2:1`) (finesse, fire, magical, reach 20 ft., unarmed), **Damage** 1d12+9 piercing plus 3d8 fire plus 2d10 fire"
  - name: "Melee strike"
    desc: "Talon +30 (`pf2:1`) (agile, finesse, fire, magical, reach 20 ft., unarmed), **Damage** 1d6+6 piercing plus 3d8 fire plus 2d10 fire"
  - name: "Ranged strike"
    desc: "Flame Jet +30 (`pf2:1`) (fire, range 40 ft.), **Damage** 6d6 fire plus 2d10 fire"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 39, attack +31<br>**5th** [[Divine Immolation]]<br>**4th** [[Wall of Fire]]<br>**2nd** [[Cleanse Affliction]], [[Cleanse Affliction]], [[Dispel Magic]], [[Dispel Magic]] (At Will), [[Everlight]] (At Will), [[See the Unseen]] (Constant)<br>**1st** [[Detect Magic]] (Constant), [[Heal]], [[Light]]"
abilities_bot:
  - name: "Flaming Strafe"
    desc: "`pf2:1` The phoenix blazes with superheated flame and Flies up to their Speed. They deal 6d6 fire damage to each creature within 20 feet of each square they move through (DC 37 [[Reflex]] save)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The phoenix is a primordial bird made of heat and flame that dwells in the most inhospitable regions of the desert. Though highly intelligent and usually brimming with compassion, phoenixes are best known for their iconic ability to resurrect themselves when slain, emerging reborn from the ashes of their own corpses. Phoenixes are often sought out for their knowledge of healing abilities, as they cannot abide the sight of suffering and deny their succor only to the most foul and irredeemable of creatures.

Phoenixes enjoy the company of peaceful dragons, and the two can forge lifelong friendships, keeping each other updated on regional news.

While most phoenixes are benevolent, they are not infallible. When a phoenix loses their way, they still retain their strong appetite for knowledge. Malevolent phoenixes are known to assault universities and libraries in their pursuit for power—not only to gain new information, but also to set fire to the texts and thus hoard that knowledge for themselves.

```statblock
creature: "Phoenix"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
