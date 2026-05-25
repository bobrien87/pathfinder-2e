---
type: creature
group: ["Archon", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aesra"
level: "7"
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
languages: "Diabolic, Draconic, Empyrean, Utopian (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +13, Arcana +14, Diplomacy +16, Intimidation +16, Religion +13, Survival +14"
abilityMods: ["+5", "+2", "+4", "+1", "+2", "+5"]
abilities_top:
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Flame of Justice"
    desc: "An aesra's spirit of righteousness manifests as a two-handed sword of fire. If disarmed or thrown as a ranged weapon, the flame of justice vanishes after landing or dealing damage and reappears in the aesra's hands again instantly. On a critical hit, the target also takes 2d6 persistent,fire damage."
  - name: "Maintain Formation"
    desc: "When an aesra casts [[Translocate]], they can bring an adjacent willing archon along with them. That archon appears in an empty space adjacent to the aesra's new space."
armorclass:
  - name: AC
    desc: "27 all-around vision; **Fort** +17, **Ref** +11, **Will** +15"
health:
  - name: HP
    desc: "100; **Immunities** fear effects; **Weaknesses** unholy 10; **Resistances** fire 15"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Archon's Protection"
    desc: "`pf2:r` **Trigger** An enemy damages the archon's ally and both are within 15 feet of the archon <br>  <br> **Effect** The ally gains resistance 10 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Flame of Justice +18 (`pf2:1`) (holy, magical, versatile p), **Damage** 1d6 fire plus 2d10+5 slashing plus [[Flame Of Justice]]"
  - name: "Ranged strike"
    desc: "Flame of Justice +15 (`pf2:1`) (holy, magical, versatile p, range 30 ft.), **Damage** 1d6 fire plus 2d10+5 slashing plus [[Flame Of Justice]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24, attack +16<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Translocate]] (At Will)<br>**1st** [[Light]], [[Message]], [[Sure Strike]]"
abilities_bot:
  - name: "Flaming Slash"
    desc: "`pf2:2` The aesra sweeps their sword, creating a @Template[cone|distance:15] of sacred flame that deals @Damage[5d6[fire]|options:area-damage] damage with a DC 23 [[Reflex]] save."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Despite their flaming blades and ring of unblinking eyes, aesras are the diplomats of peace among the archons, preferring justice via compromise and mutual benefit rather than justice by the sword. Nonetheless, when forced to fight against fiendish powers aesras don't hesitate in battle, mounting offensives under divine commanders like Iomedae.

Archons are guardians of Heaven and enemies of corruption. Before gods and their servants set foot in the celestial planes, archons already resided in Heaven, the original inhabitants of the realm. Upon meeting, the archons and divine angels quickly discovered they were of a kind, holding justice and righteousness in their hearts. An alliance was formed, and archons now serve as stalwart allies to all celestials and mortals they find worthy.

While the first archons coalesced from the immense seven-tiered mountain of Heaven, they choose willing and worthy Heaven-bound souls to join their ranks. These mortals hear and answer the call of a mysterious voice, manifesting in the Garden at the mountain's peak. There they swear to forever serve the cause of justice and transform into their new archon forms.

Though deeply concerned with defending mortal life and willing to sacrifice themselves in battle against fiends, archons often feel rote and inscrutable to others, and their forms can border on frightening and bizarre. For this reason, they often have issues with interacting with mortals, or with the free spirited azatas. Despite this, archons draw great strength from others, especially those who exemplify virtue.

Beyond their celestial allies, archons also maintain ancient ties with aeons. The inscrutable factions can still be seen working together to defend longforgotten secrets and enforce rules that predate mortal life. Archons explain these missions as necessary without further elaboration, leaving even their angelic allies frustrated with archons' obstinance.

```statblock
creature: "Aesra"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
