---
type: creature
group: ["Archon", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zoaem"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean, Utopian"
skills:
  - name: Skills
    desc: "Acrobatics +8, Intimidation +6, Religion +6"
abilityMods: ["-5", "+3", "+1", "-1", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16 all-around vision; **Fort** +6, **Ref** +10, **Will** +4"
health:
  - name: HP
    desc: "20; **Immunities** fear effects; **Weaknesses** unholy 3; **Resistances** fire 3"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Archon's Protection"
    desc: "`pf2:r` **Trigger** An enemy damages the archon's ally and both are within 15 feet of the archon <br>  <br> **Effect** The ally gains resistance 3 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "0 feet"
attacks:
  - name: "Ranged strike"
    desc: "Eye Ray +8 (`pf2:1`) (agile, fire, holy, magical), **Damage** 1d8 fire"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**4th** [[Read Omens]]<br>**1st** [[Heal]], [[Light]]"
abilities_bot:
  - name: "Behold!"
    desc: "`pf2:2` **Frequency** once per hour; <br>  <br> **Effect** The zoaem's rings and wings move in a complex pattern, mesmerizing creatures in the zoaem's choice of a @Template[emanation|distance:10] or a @Template[burst|distance:5] within 60 feet. Each creature must succeed at a DC 17 [[Will]] save or be [[Fascinated]] with the zoaem for 1 minute and [[Stunned]] 1 (or stunned for 1 round on a critical failure)."
  - name: "Light of Truth"
    desc: "`pf2:1` The zoaem shines an intense light of truth, as [[Revealing Light]] (DC 17 [[Reflex]] save) but in a @Template[line|distance:60]. Against creatures affected by this light, the zoaem and their allies gain a +1 status bonus to damage rolls and Recall Knowledge checks. The zoaem can't use Light of Truth again for 1d4 rounds. <br>  <br> > [!danger] Effect: Light of Truth"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These endlessly curious archons are formed from spinning wheels of golden light given corporeal shape. They serve as lookouts and mobile support troops for the archon legions, at times uniting to form powerful warriors of light called gestalts. Larger collectives of zoaems can even temporarily fuse into greater archons, approaching the power of the first zoaem, which broke itself apart to serve Heaven more efficiently.

Archons are guardians of Heaven and enemies of corruption. Before gods and their servants set foot in the celestial planes, archons already resided in Heaven, the original inhabitants of the realm. Upon meeting, the archons and divine angels quickly discovered they were of a kind, holding justice and righteousness in their hearts. An alliance was formed, and archons now serve as stalwart allies to all celestials and mortals they find worthy.

While the first archons coalesced from the immense seven-tiered mountain of Heaven, they choose willing and worthy Heaven-bound souls to join their ranks. These mortals hear and answer the call of a mysterious voice, manifesting in the Garden at the mountain's peak. There they swear to forever serve the cause of justice and transform into their new archon forms.

Though deeply concerned with defending mortal life and willing to sacrifice themselves in battle against fiends, archons often feel rote and inscrutable to others, and their forms can border on frightening and bizarre. For this reason, they often have issues with interacting with mortals, or with the free spirited azatas. Despite this, archons draw great strength from others, especially those who exemplify virtue.

Beyond their celestial allies, archons also maintain ancient ties with aeons. The inscrutable factions can still be seen working together to defend longforgotten secrets and enforce rules that predate mortal life. Archons explain these missions as necessary without further elaboration, leaving even their angelic allies frustrated with archons' obstinance.

```statblock
creature: "Zoaem"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
