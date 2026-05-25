---
type: creature
group: ["Astral"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shining Child"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Astral"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+23; [[Darkvision]]"
languages: "Aklo (Telepathy 120 feet)"
skills:
  - name: Skills
    desc: "Arcana +18, Deception +23, Diplomacy +21, Intimidation +21, Occultism +18"
abilityMods: ["+2", "+5", "+6", "+2", "+5", "+7"]
abilities_top:
  - name: "Telepathy 120 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Radiance Dependence"
    desc: "The shining child is [[Off Guard]] while in areas of darkness."
armorclass:
  - name: AC
    desc: "33; **Fort** +22, **Ref** +19, **Will** +19"
health:
  - name: HP
    desc: "215; **Immunities** blinded, dazzled, fire"
abilities_mid:
  - name: "Blinding Aura"
    desc: "60 feet. <br>  <br> The shining child sheds bright light. Any creature that starts its turn in the aura must succeed at a DC 29 [[Fortitude]] save. If it fails, it is [[Blinded]] for 1 minute, and if it critically fails, it's permanently blinded. A creature that succeeds at its save is temporarily immune to this effect for 24 hours."
  - name: "Overwhelming Light"
    desc: "`pf2:r` **Trigger** The shining child enters an area of magical darkness or begins its turn in an area of magical darkness <br>  <br> **Effect** The shining child attempts to counteract the magical darkness (counteract rank 7, counteract modifier +23)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +25 (`pf2:1`) (agile, finesse, magical, unarmed), **Damage** 3d4+5 bludgeoning plus 4d6 fire plus 2d4 fire"
  - name: "Ranged strike"
    desc: "Fire Ray +25 (`pf2:1`) (arcane, magical), **Damage** 3d10+3 fire"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33, attack +25<br>**7th** [[Sunburst]]<br>**6th** [[Vibrant Pattern]], [[Wall of Force]]<br>**5th** [[False Vision]]<br>**4th** [[Mirage]], [[Translocate]], [[Translocate]] (At Will)<br>**2nd** [[Dispel Magic]]<br>**1st** [[Illusory Object]] (At Will), [[Light]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Shining children are wicked, enigmatic monsters that roam remote planes and untraveled corners of the universe in search of esoteric lore. With their abnormally gaunt frames, long white hair, and unnerving, four-fingered hands, shining children are both strangely familiar and otherworldly in appearance, though they are barely visible within the shroud of blinding light they continually emit. Their faces are truly horrible, however, as their overlarge eyes and distended, gaping mouths reveal their heads to be voids filled with unnatural light. Shining children use this light as a weapon, weaving illusions and focusing beams of fiery brilliance.

Because of their reputation as scholars of the alien and the eldritch, shining children are sometimes summoned by powerful wizards or occultists in search of rare knowledge. The creatures never give away their lore without some price, though, and typically demand in return the performance of contemptible deeds that further their inscrutable, far-ranging plans.

These mysterious beings are natives of the Astral Plane. In that vast plane, accretions of metaphysical matter gradually accumulate and eventually coalesce into demiplanes. During this tumultuous process, sparks of living light sometimes shear off the newly formed planes, and these sparks of raw planar energy somehow transform into shining children. Every newly formed demiplane leaves a different mental imprint on its shining "offspring," making it easy for shining children to telepathically recognize their brothers and sisters. Forever trapped in apparently adolescent bodies, shining children dedicate themselves to scholarship and violence with equal measure in a futile effort to understand their roles in the multiverse and the burning injustice of their births.

Shining children confuse most other creatures with their refusal to use individual names in favor of alternating between referring to each other singularly and collectively.

```statblock
creature: "Shining Child"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
