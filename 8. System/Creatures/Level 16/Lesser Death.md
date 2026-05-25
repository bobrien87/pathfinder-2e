---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lesser Death"
level: "16"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+32; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +33, Athletics +28, Deception +30, Intimidation +32, Religion +30, Society +26, Stealth +35"
abilityMods: ["+6", "+9", "+6", "+4", "+6", "+6"]
abilities_top:
  - name: "Death's Grace"
    desc: "The lesser death can choose whether or not it counts as undead for effects that affect undead differently. Even if it does not count as undead, the lesser death still never counts as a living creature."
  - name: "Status Sight"
    desc: "The Lesser Death automatically knows the Hit Points, conditions, afflictions, and emotions of all creatures it can see."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Infuse Weapon"
    desc: "Any scythe gains the agile trait, can't be disarmed, and becomes a *+2 greater striking keen scythe* while the lesser death wields it."
armorclass:
  - name: AC
    desc: "39; **Fort** +30, **Ref** +33, **Will** +32"
health:
  - name: HP
    desc: "255; death's grace, void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Aura of Misfortune"
    desc: "20 feet. <br>  <br> Living creatures in the aura must roll twice on all d20 rolls and use the lower result. <br>  <br> > [!danger] Effect: Aura of Misfortune"
  - name: "Lurking Death"
    desc: "`pf2:r` **Trigger** A creature within 60 feet makes a ranged attack or uses an action that has the concentrate, manipulate, or move trait <br>  <br> **Effect** The lesser death teleports to a square adjacent to the triggering creature and makes a melee Strike against it. If the Strike hits, the lesser death disrupts the triggering action."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Keen Scythe +32 (`pf2:1`) (agile, deadly 2d10, magical, reach 10 ft., trip), **Damage** 3d10+14 slashing plus 1d12 void"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30<br>**6th** [[Truesight]] (Constant)<br>**2nd** [[See the Unseen]] (Constant)"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

No one is quite sure what lesser deaths are, though some claim that they are avatars of the Grim Reaper. Unlike that strange hunter, however, lesser deaths hunt in packs on rare occasions. More often than not, they manifest from cursed magic items. Other times, they are just the enactors of death, hunting in the same way the Grim Reaper does—silently, with no remorse or quarter. Rarely, multiple lesser deaths work together to cull a large population, their scythes cutting through crowds and leaving entire cities devoid of life, inspiring (hopefully) false rumors of multiple Grim Reapers.

The Grim Reaper is the unflinching personification of death. Silent as the grave and as inevitable as time itself, this legendary being hunts down and finishes creatures that have evaded death for far too long. Sometimes the Grim Reaper comes without warning, while at others it comes to finish the work that other creatures could not. The Grim Reaper serves no god, fiend, or aeon. It is both despised and feared by psychopomps and celestials, but few-if any-dare to stand in its way. Like some eternal plague, it kills those who try to cure the multiverse of its presence. It stands alone and holds only its own council, and the pleading and reasoning of mortals and immortals alike fall on deaf ears once the Grim Reaper closes on its quarry. Its own reasoning is silent to mortal ears and inscrutable to the mortal mind, but no matter the reason, the result is unyielding and final.

While some legends hold that the Grim Reaper appears before everyone as they die, the truth is quite a bit more disturbing. Such vigils in fact lie within the providence of the psychopomps, a race of immortals charged with the protection and guidance of mortal souls through the afterlife. The Grim Reaper has little interest in protecting souls or guiding them. It is instead compelled by sinister agendas arising within the nighted realm of Abaddon, where the Horsemen of the Apocalypse rule. Indeed there are many similarities in shape and form between the Grim Reaper and Charon, the Horseman of Death, but no recorded instance exists of these two powerful entities working together. Instead, the Grim Reaper serves as something of a manifestation of Abaddon itself, and in this regard is believed by some to be an incarnation of the mysterious First Horseman. When the Grim Reaper comes to a world, it does so not as an angel of mercy, but as a relentless harvester of life. Those who fall to the Grim Reaper were not destined to die as much as they were selected, hunted, and murdered.

Perhaps the most frightening legends surrounding the Grim Reaper concern its nature as a singular entity, for some believe that more than one grim reaper exists in the Great Beyond. These whispers tell of a cabal of at least nine of these creatures that stalk reality, culling the living as inexplicable servants of true entropy. According to the teaching of some death cults, the final goal of the Grim Reaper is to end the entire cycle of life and death and serve as a silent lord of an empty universe.

```statblock
creature: "Lesser Death"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
