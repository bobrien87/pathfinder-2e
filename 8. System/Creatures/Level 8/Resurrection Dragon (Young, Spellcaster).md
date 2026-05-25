---
type: creature
group: ["Divine", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Resurrection Dragon (Young, Spellcaster)"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +15, Arcana +15, Athletics +18, Diplomacy +18, Medicine +18, Religion +18, Stealth +17, Necromancy Lore +19"
abilityMods: ["+6", "+3", "+4", "+3", "+6", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "26; **Fort** +15, **Ref** +14, **Will** +19"
health:
  - name: HP
    desc: "140; **Immunities** death effects, paralyzed, sleep; **Resistances** spirit 10"
abilities_mid:
  - name: "Reawaken!"
    desc: "`pf2:r` **Trigger** A living creature the resurrection dragon can see dies <br>  <br> **Effect** The resurrection dragon uses divine and vital energy to retether the soul to its dead body. The willing creature is returned to life with the [[Dying]] 1 condition at the start of its next turn. A creature can be resurrected by this ability only once."
  - name: "Risen Commander"
    desc: "A resurrection dragon has a strong connection with its minions and can Sustain [[Summon Undead]] or [[Invoke Spirits]] as a free action once per turn."
  - name: "Siphon Life"
    desc: "`pf2:r` **Trigger** A creature within 60 feet uses a healing effect that restores Hit Points <br>  <br> **Effect** The resurrection dragon redirects vital energies away from the effect, minimizing its impact. The triggering effect results in the minimum amount on any dice rolls to restore Hit Points, and any flat values for restoring Hit Points (such as the additional Hit Points for a two-action [[Heal]] spell) are cut in half. The dragon then gains 1d8 temporary Hit Points that last for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d10+9 piercing plus 1d6 void"
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, magical), **Damage** 2d8+9 slashing"
  - name: "Melee strike"
    desc: "Tail +18 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d10+9 bludgeoning"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 26, attack +18<br>**3rd** (3 slots) [[Final Sacrifice]], [[Sudden Blight]], [[Vampiric Feast]]<br>**2nd** (3 slots) [[Heal]], [[Share Life]], [[Spirit Sense]]<br>**1st** (3 slots) [[Command]], [[Infuse Vitality]], [[Grim Tendrils]]<br>**Cantrips** [[Detect Magic]], [[Guidance]], [[Haunting Hymn]], [[Read Aura]], [[Stabilize]]"
  - name: "Divine Innate Spells"
    desc: "DC 26, attack +0<br>**4th** [[Talking Corpse]]<br>**1st** [[Guidance]], [[Harm]], [[Stabilize]], [[Summon Undead]] (At Will), [[Void Warp]]"
abilities_bot:
  - name: "Soul Siphoning Breath"
    desc: "`pf2:2` The dragon unleashes a torrent of divine energy, dealing @Damage[7d6[void]|options:area-damage] damage in a @Template[type:cone|distance:30] (DC 26 [[Fortitude]] save) that draws the life force from creatures within. The dragon gains fast healing 5 until their Soul Siphoning Breath recharges. The resurrection dragon can't use Soul Siphoning Breath again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Resurrection dragons teeter between life and death. They have a mastery of vital energies, allowing them to restore life to the dead, and a mastery of void energies, to bestow death on others. They make use of their abilities to play with the lives of mortals, calling on spirits to aid them or reviving creatures they find important or interesting. The lair of a resurrection dragon is generally a barren place. While they still hoard wealth like other dragons, they do little to decorate their lairs and treasures are generally kept in dark niches, as if the dragon has little care for their possessions. Resurrection dragons tend to take tokens from those they resurrect or plan to resurrect, however, and these are kept particularly safe.

```statblock
creature: "Resurrection Dragon (Young, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
