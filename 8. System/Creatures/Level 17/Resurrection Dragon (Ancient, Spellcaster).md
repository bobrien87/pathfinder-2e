---
type: creature
group: ["Divine", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Resurrection Dragon (Ancient, Spellcaster)"
level: "17"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+32; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +28, Arcana +28, Athletics +33, Diplomacy +31, Medicine +33, Religion +33, Stealth +30, Necromancy Lore +36"
abilityMods: ["+9", "+5", "+6", "+5", "+9", "+6"]
abilities_top:
  - name: "Arise!"
    desc: "The resurrection dragon uses their mastery over life energy to cast their own soul into the Boneyard and pull a willing creature's soul back to its body in a process that takes 1 hour. This has the effects of [[Raise Dead]], except the maximum level of the target is 13th and the soul is tethered to the dragon's. Only one creature can be tethered to the dragon's soul at a time. If the creature and the dragon are no longer on the same plane or the dragon dies, the raised creature dies and can't be raised with Arise! again. The dragon can Dismiss the connection at any time. Doing so doesn't prevent the dragon from raising the creature with Arise! again. <br>  <br> While raised in this way, the creature is still a valid target for *raise dead*, [[Resurrect]], and similar effects. Returning the creature to life in this way fully restores the creature, severing the connection to the dragon and allowing the dragon to establish a connection with a different creature."
armorclass:
  - name: AC
    desc: "39; **Fort** +28, **Ref** +27, **Will** +32"
health:
  - name: HP
    desc: "320; **Immunities** death effects, paralyzed, sleep; **Resistances** spirit 20"
abilities_mid:
  - name: "Reawaken!"
    desc: "`pf2:r` **Trigger** A living creature the resurrection dragon can see dies <br>  <br> **Effect** The resurrection dragon uses divine and vital energy to retether the soul to its dead body. The willing creature is returned to life with half of their total Hit Points. A creature can be resurrected by this ability only once."
  - name: "Risen Commander"
    desc: "A resurrection dragon has a strong connection with its minions and can Sustain [[Summon Undead]] or [[Invoke Spirits]] as a free action once per turn."
  - name: "Siphon Life"
    desc: "`pf2:r` **Trigger** A creature within 60 feet uses a healing effect that restores Hit Points <br>  <br> **Effect** The resurrection dragon redirects vital energies away from the effect, minimizing its impact. The triggering effect results in the minimum amount on any dice rolls to restore Hit Points, and any flat values for restoring Hit Points (such as the additional Hit Points for a two-action [[Heal]] spell) are cut in half. The dragon then gains 3d8 temporary Hit Points that last for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +33 (`pf2:1`) (magical, reach 15 ft.), **Damage** 3d12+15 piercing plus 1d6 void"
  - name: "Melee strike"
    desc: "Claw +33 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 3d10+15 slashing"
  - name: "Melee strike"
    desc: "Tail +31 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d12+15 bludgeoning"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 38, attack +30<br>**8th** (3 slots) [[Moment of Renewal]], [[Raise Dead]], [[Summon Undead]]<br>**7th** (3 slots) [[Execute]], [[Harm]], [[Regenerate]]<br>**6th** (3 slots) [[Field of Life]], [[Raise Dead]], [[Summon Undead]]<br>**5th** (3 slots) [[Dispel Magic]], [[Heal]], [[Invoke Spirits]]<br>**4th** (3 slots) [[Harm]], [[Summon Undead]], [[Talking Corpse]]<br>**3rd** (3 slots) [[Final Sacrifice]], [[Sudden Blight]], [[Vampiric Feast]]<br>**2nd** (3 slots) [[Heal]], [[Share Life]], [[Spirit Sense]]<br>**1st** (3 slots) [[Command]], [[Infuse Vitality]], [[Grim Tendrils]]<br>**Cantrips** [[Detect Magic]], [[Guidance]], [[Haunting Hymn]], [[Read Aura]], [[Stabilize]]"
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +0<br>**6th** [[Raise Dead]]<br>**5th** [[Invoke Spirits]]<br>**4th** [[Talking Corpse]] (At Will)<br>**1st** [[Guidance]], [[Harm]], [[Stabilize]], [[Summon Undead]] (At Will), [[Void Warp]]"
abilities_bot:
  - name: "Necro Puppeteer"
    desc: "`pf2:2` The dragon siphons energy into an undead creature, a dying creature, or a corpse they can see within 60 feet. The dragon moves the target creature 30 feet and causes it to unleash a wave of void energy in a @Template[type:emanation|distance:10], dealing @Damage[6d8[void]|options:area-damage] damage (DC 32 [[Reflex]] save)."
  - name: "Soul Siphoning Breath"
    desc: "`pf2:2` The dragon unleashes a torrent of divine energy, dealing @Damage[16d6[void]|options:area-damage] damage in a @Template[type:cone|distance:50] (DC 38 [[Fortitude]] save) that draws the life force from creatures within. The dragon gains fast healing 15 until their Soul Siphoning Breath recharges. The resurrection dragon can't use Soul Siphoning Breath again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Resurrection dragons teeter between life and death. They have a mastery of vital energies, allowing them to restore life to the dead, and a mastery of void energies, to bestow death on others. They make use of their abilities to play with the lives of mortals, calling on spirits to aid them or reviving creatures they find important or interesting. The lair of a resurrection dragon is generally a barren place. While they still hoard wealth like other dragons, they do little to decorate their lairs and treasures are generally kept in dark niches, as if the dragon has little care for their possessions. Resurrection dragons tend to take tokens from those they resurrect or plan to resurrect, however, and these are kept particularly safe.

```statblock
creature: "Resurrection Dragon (Ancient, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
